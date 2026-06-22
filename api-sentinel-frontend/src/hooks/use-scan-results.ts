import { useQuery } from "@tanstack/react-query";

import {
  getScanResults,
} from "@/services/scan-results";

export const useScanResults = (
  scanId: string
) => {
  return useQuery({
    queryKey: [
      "scan-results",
      scanId,
    ],

    queryFn: () =>
      getScanResults(scanId),
  });
};