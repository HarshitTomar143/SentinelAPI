"use client";

import { useEffect } from "react";
import { useParams, useRouter } from "next/navigation";

import { Card } from "@/components/ui/card";
import { useScanStatus } from "@/hooks/use-scan-status";

export default function ScanPage() {
  const params = useParams();
  const router = useRouter();

  const scanId = params.id as string;

  const {
    data,
    isLoading,
    error,
  } = useScanStatus(scanId);

  useEffect(() => {
    if (data?.data.status === "completed") {
      router.push(`/scans/${scanId}/report`);
    }
  }, [data, router, scanId]);

  if (isLoading) {
    return (
      <div className="p-6">
        Loading scan...
      </div>
    );
  }

  if (error) {
    console.error(error);

    return (
      <div className="p-6">
        Something went wrong
      </div>
    );
  }

  return (
    <div className="flex min-h-screen items-center justify-center p-6">
      <Card className="w-full max-w-md p-6">
        <h1 className="text-2xl font-bold">
          Scan Status
        </h1>

        <p className="mt-4">
          Scan ID:
        </p>

        <p className="font-mono break-all">
          {data?.data.scan_id}
        </p>

        <p className="mt-4">
          Status:
        </p>

        <p className="capitalize">
          {data?.data.status}
        </p>

        <p className="mt-4">
          Progress:
        </p>

        <p>
          {data?.data.progress}%
        </p>

        <div className="mt-2 h-3 w-full rounded-full bg-muted">
          <div
            className="h-3 rounded-full bg-primary transition-all duration-500"
            style={{
              width: `${data?.data.progress ?? 0}%`,
            }}
          />
        </div>

        <p className="mt-4">
          Current Stage:
        </p>

        <p>
          {data?.data.current_stage}
        </p>
      </Card>
    </div>
  );
}