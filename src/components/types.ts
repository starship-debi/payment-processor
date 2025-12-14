// types.ts
import { PaymentMethod } from './payment-method';
import { PaymentStatus } from './payment-status';

export enum PaymentType {
  CREDIT_CARD = 'credit_card',
  DEBIT_CARD = 'debit_card',
  BANK_TRANSFER = 'bank_transfer',
}

export interface PaymentRequest {
  id: string;
  paymentMethod: PaymentMethod;
  amount: number;
  paymentType: PaymentType;
  description: string;
}

export interface PaymentResponse {
  id: string;
  paymentMethod: PaymentMethod;
  amount: number;
  paymentType: PaymentType;
  status: PaymentStatus;
  description: string;
  timestamp: Date;
}

export interface PaymentMethod {
  id: string;
  type: PaymentType;
  cardNumber: string;
  expiryDate: string;
  cvv: string;
  name: string;
  email: string;
}

export interface PaymentStatus {
  id: string;
  name: string;
  description: string;
}

export interface PaymentError {
  id: string;
  message: string;
  code: number;
  timestamp: Date;
}