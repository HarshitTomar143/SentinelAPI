import { useQuery } from "@tanstack/react-query";
import { getScanStatus } from "@/services/scan-status";

export const useScanStatus = (scanId: string) => {
  return useQuery({
    queryKey: ["scan-status", scanId],

    queryFn: () => getScanStatus(scanId),

    refetchInterval: 3000,
  });
};