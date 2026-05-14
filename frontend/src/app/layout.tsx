import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Metsenat Frontend Service",
  description: "Next.js frontend for Metsenat backend API integration",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
