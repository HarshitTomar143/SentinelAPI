"use client"

import {QueryClient, QueryClientProvider,} from "@tanstack/react-query";
import { ReactNode } from "react";

const queryClient = new QueryClient({
    defaultOptions : {
        queries: {
            retry: 1,
            staleTime: 1000 * 30,
        }
    }
});
interface Props {
    children :ReactNode
} 

export function QueryProvider({
    children,
}: Props){
    return (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  );
}