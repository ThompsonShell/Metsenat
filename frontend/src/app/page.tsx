"use client";

import { FormEvent, useCallback, useMemo, useState } from "react";
import {
  ApiError,
  createAppeal,
  createPaymentMethod,
  createStudentSponsor,
  createUniversity,
  getApiBaseUrl,
  listAppeals,
  listPaymentMethods,
  listStudentSponsors,
  listUniversities,
  listUsers,
  loginWithPassword,
  sendVerificationCode,
} from "@/lib/api";
import type { Appeal, PaymentMethod, StudentSponsor, University, User } from "@/types/api";
import styles from "./page.module.css";

const TOKEN_STORAGE_KEY = "metsenat_access_token";

type FormMessage = { type: "success" | "error"; text: string } | null;

function parseError(error: unknown): string {
  if (error instanceof ApiError) {
    return `${error.message} (status: ${error.status})`;
  }
  if (error instanceof Error) {
    return error.message;
  }
  return "Unknown error";
}

export default function Home() {
  const [token, setToken] = useState(() => {
    if (typeof window === "undefined") {
      return "";
    }
    return window.localStorage.getItem(TOKEN_STORAGE_KEY) ?? "";
  });
  const [phoneNumber, setPhoneNumber] = useState("");
  const [password, setPassword] = useState("");

  const [users, setUsers] = useState<User[]>([]);
  const [universities, setUniversities] = useState<University[]>([]);
  const [paymentMethods, setPaymentMethods] = useState<PaymentMethod[]>([]);
  const [appeals, setAppeals] = useState<Appeal[]>([]);
  const [studentSponsors, setStudentSponsors] = useState<StudentSponsor[]>([]);

  const [newUniversityName, setNewUniversityName] = useState("");
  const [newUniversityAmount, setNewUniversityAmount] = useState("");
  const [newPaymentMethodName, setNewPaymentMethodName] = useState("");

  const [appealPhone, setAppealPhone] = useState("");
  const [appealAmount, setAppealAmount] = useState("");
  const [appealAvailable, setAppealAvailable] = useState("");
  const [appealSponsorId, setAppealSponsorId] = useState("");
  const [appealPaymentMethodId, setAppealPaymentMethodId] = useState("");

  const [studentId, setStudentId] = useState("");
  const [sponsorId, setSponsorId] = useState("");
  const [sponsorAmount, setSponsorAmount] = useState("");

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<FormMessage>(null);

  const dashboard = useMemo(() => {
    const appealsAmount = appeals.reduce((total, item) => total + Number(item.amount), 0);
    const sponsorshipAmount = studentSponsors.reduce((total, item) => total + Number(item.amount), 0);

    return {
      users: users.length,
      universities: universities.length,
      paymentMethods: paymentMethods.length,
      appeals: appeals.length,
      studentSponsors: studentSponsors.length,
      appealsAmount,
      sponsorshipAmount,
    };
  }, [appeals, paymentMethods.length, studentSponsors, universities.length, users.length]);

  const reloadData = useCallback(async (activeToken: string = "") => {
    setLoading(true);
    setMessage(null);

    try {
      const [loadedUniversities, loadedPaymentMethods, loadedAppeals, loadedSponsors] =
        await Promise.all([
          listUniversities(),
          listPaymentMethods(),
          listAppeals(),
          listStudentSponsors(),
        ]);

      setUniversities(loadedUniversities);
      setPaymentMethods(loadedPaymentMethods);
      setAppeals(loadedAppeals);
      setStudentSponsors(loadedSponsors);

      if (activeToken) {
        const loadedUsers = await listUsers(activeToken);
        setUsers(loadedUsers);
      } else {
        setUsers([]);
      }

      setMessage({ type: "success", text: "API data loaded successfully." });
    } catch (error) {
      setMessage({ type: "error", text: parseError(error) });
    } finally {
      setLoading(false);
    }
  }, []);

  async function handleLogin(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    setMessage(null);

    try {
      const result = await loginWithPassword(phoneNumber, password);
      setToken(result.access);
      window.localStorage.setItem(TOKEN_STORAGE_KEY, result.access);
      await reloadData(result.access);
      setMessage({ type: "success", text: "Login successful, token saved locally." });
    } catch (error) {
      setMessage({ type: "error", text: parseError(error) });
    } finally {
      setLoading(false);
    }
  }

  async function handleSendCode() {
    setLoading(true);
    setMessage(null);

    try {
      await sendVerificationCode(phoneNumber);
      setMessage({ type: "success", text: "Verification code request sent." });
    } catch (error) {
      setMessage({ type: "error", text: parseError(error) });
    } finally {
      setLoading(false);
    }
  }

  async function handleCreateUniversity(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    try {
      setLoading(true);
      await createUniversity(
        { name: newUniversityName, contract_amount: newUniversityAmount },
        token || undefined,
      );
      setNewUniversityName("");
      setNewUniversityAmount("");
      await reloadData(token);
    } catch (error) {
      setMessage({ type: "error", text: parseError(error) });
    } finally {
      setLoading(false);
    }
  }

  async function handleCreatePaymentMethod(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    try {
      setLoading(true);
      await createPaymentMethod({ name: newPaymentMethodName }, token || undefined);
      setNewPaymentMethodName("");
      await reloadData(token);
    } catch (error) {
      setMessage({ type: "error", text: parseError(error) });
    } finally {
      setLoading(false);
    }
  }

  async function handleCreateAppeal(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    try {
      setLoading(true);
      await createAppeal(
        {
          phone_number: appealPhone,
          amount: appealAmount,
          available: appealAvailable,
          status: 2,
          sponsor: Number(appealSponsorId),
          payment_method: Number(appealPaymentMethodId),
        },
        token || undefined,
      );
      setAppealPhone("");
      setAppealAmount("");
      setAppealAvailable("");
      await reloadData(token);
    } catch (error) {
      setMessage({ type: "error", text: parseError(error) });
    } finally {
      setLoading(false);
    }
  }

  async function handleCreateStudentSponsor(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    try {
      setLoading(true);
      await createStudentSponsor(
        {
          sponsor: Number(sponsorId),
          student: Number(studentId),
          amount: sponsorAmount,
        },
        token || undefined,
      );
      setSponsorId("");
      setStudentId("");
      setSponsorAmount("");
      await reloadData(token);
    } catch (error) {
      setMessage({ type: "error", text: parseError(error) });
    } finally {
      setLoading(false);
    }
  }

  function logout() {
    setToken("");
    setUsers([]);
    window.localStorage.removeItem(TOKEN_STORAGE_KEY);
    setMessage({ type: "success", text: "Token removed from local storage." });
  }

  return (
    <main className={styles.page}>
      <header className={styles.header}>
        <h1>Metsenat Frontend Service (Next.js)</h1>
        <p>Backend API base URL: {getApiBaseUrl()}</p>
      </header>

      <section className={styles.section}>
        <h2>Auth + API check</h2>
        <form className={styles.gridForm} onSubmit={handleLogin}>
          <input
            value={phoneNumber}
            onChange={(event) => setPhoneNumber(event.target.value)}
            placeholder="Phone number (+998...)"
            required
          />
          <input
            type="password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
            placeholder="Password"
            required
          />
          <div className={styles.actions}>
            <button type="submit" disabled={loading}>
              Login (JWT)
            </button>
            <button type="button" onClick={handleSendCode} disabled={loading || !phoneNumber}>
              Send Verification Code
            </button>
            <button type="button" onClick={() => reloadData(token)} disabled={loading}>
              Reload API Data
            </button>
            <button type="button" onClick={logout} disabled={loading || !token}>
              Logout
            </button>
          </div>
        </form>

        {message ? (
          <p className={message.type === "success" ? styles.success : styles.error}>{message.text}</p>
        ) : null}
      </section>

      <section className={styles.section}>
        <h2>Dashboard</h2>
        <div className={styles.cards}>
          <article>
            <strong>{dashboard.users}</strong>
            <span>Users (requires JWT)</span>
          </article>
          <article>
            <strong>{dashboard.universities}</strong>
            <span>Universities</span>
          </article>
          <article>
            <strong>{dashboard.paymentMethods}</strong>
            <span>Payment Methods</span>
          </article>
          <article>
            <strong>{dashboard.appeals}</strong>
            <span>Appeals</span>
          </article>
          <article>
            <strong>{dashboard.studentSponsors}</strong>
            <span>Student Sponsors</span>
          </article>
          <article>
            <strong>{dashboard.appealsAmount.toFixed(2)}</strong>
            <span>Total Appeal Amount</span>
          </article>
          <article>
            <strong>{dashboard.sponsorshipAmount.toFixed(2)}</strong>
            <span>Total Sponsorship Amount</span>
          </article>
        </div>
      </section>

      <section className={styles.section}>
        <h2>Create university</h2>
        <form className={styles.inlineForm} onSubmit={handleCreateUniversity}>
          <input
            value={newUniversityName}
            onChange={(event) => setNewUniversityName(event.target.value)}
            placeholder="University name"
            required
          />
          <input
            value={newUniversityAmount}
            onChange={(event) => setNewUniversityAmount(event.target.value)}
            placeholder="Contract amount"
            required
          />
          <button type="submit" disabled={loading}>
            Create
          </button>
        </form>
      </section>

      <section className={styles.section}>
        <h2>Create payment method</h2>
        <form className={styles.inlineForm} onSubmit={handleCreatePaymentMethod}>
          <input
            value={newPaymentMethodName}
            onChange={(event) => setNewPaymentMethodName(event.target.value)}
            placeholder="Payment method name"
            required
          />
          <button type="submit" disabled={loading}>
            Create
          </button>
        </form>
      </section>

      <section className={styles.section}>
        <h2>Create appeal</h2>
        <form className={styles.inlineForm} onSubmit={handleCreateAppeal}>
          <input
            value={appealPhone}
            onChange={(event) => setAppealPhone(event.target.value)}
            placeholder="Phone number"
            required
          />
          <input
            value={appealAmount}
            onChange={(event) => setAppealAmount(event.target.value)}
            placeholder="Amount"
            required
          />
          <input
            value={appealAvailable}
            onChange={(event) => setAppealAvailable(event.target.value)}
            placeholder="Available"
            required
          />
          <input
            value={appealSponsorId}
            onChange={(event) => setAppealSponsorId(event.target.value)}
            placeholder="Sponsor user ID"
            required
          />
          <input
            value={appealPaymentMethodId}
            onChange={(event) => setAppealPaymentMethodId(event.target.value)}
            placeholder="Payment method ID"
            required
          />
          <button type="submit" disabled={loading}>
            Create
          </button>
        </form>
      </section>

      <section className={styles.section}>
        <h2>Create student-sponsor relation</h2>
        <form className={styles.inlineForm} onSubmit={handleCreateStudentSponsor}>
          <input
            value={sponsorId}
            onChange={(event) => setSponsorId(event.target.value)}
            placeholder="Sponsor user ID"
            required
          />
          <input
            value={studentId}
            onChange={(event) => setStudentId(event.target.value)}
            placeholder="Student user ID"
            required
          />
          <input
            value={sponsorAmount}
            onChange={(event) => setSponsorAmount(event.target.value)}
            placeholder="Amount"
            required
          />
          <button type="submit" disabled={loading}>
            Create
          </button>
        </form>
      </section>

      <section className={styles.section}>
        <h2>Latest API items</h2>
        <div className={styles.columns}>
          <div>
            <h3>Universities</h3>
            <ul>
              {universities.slice(0, 5).map((item) => (
                <li key={item.id}>
                  #{item.id} {item.name} — {item.contract_amount}
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h3>Payment methods</h3>
            <ul>
              {paymentMethods.slice(0, 5).map((item) => (
                <li key={item.id}>
                  #{item.id} {item.name}
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h3>Appeals</h3>
            <ul>
              {appeals.slice(0, 5).map((item) => (
                <li key={item.id}>
                  #{item.id} sponsor:{item.sponsor} — {item.amount}
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h3>Student sponsors</h3>
            <ul>
              {studentSponsors.slice(0, 5).map((item) => (
                <li key={item.id}>
                  #{item.id} sponsor:{item.sponsor} → student:{item.student} — {item.amount}
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h3>Users</h3>
            <ul>
              {users.slice(0, 5).map((item) => (
                <li key={item.id}>
                  #{item.id} {item.phone_number} (role:{item.role})
                </li>
              ))}
            </ul>
          </div>
        </div>
      </section>
    </main>
  );
}
