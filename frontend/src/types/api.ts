export interface University {
  id: number;
  name: string;
  slug: string;
  contract_amount: string;
  created_at: string;
  updated_at: string;
}

export interface PaymentMethod {
  id: number;
  name: string;
  slug: string;
  created_at: string;
  updated_at: string;
}

export interface Appeal {
  id: number;
  phone_number: string;
  amount: string;
  available: string;
  status: number;
  sponsor: number;
  payment_method: number;
  created_at: string;
  updated_at: string;
}

export interface StudentSponsor {
  id: number;
  sponsor: number;
  student: number;
  amount: string;
  created_at: string;
  updated_at: string;
}

export interface User {
  id: number;
  first_name: string;
  last_name: string;
  phone_number: string;
  role: number;
  degree: number;
  user_type: number;
  balance: string;
  available: string;
}

export interface JwtTokens {
  access: string;
  refresh: string;
}
