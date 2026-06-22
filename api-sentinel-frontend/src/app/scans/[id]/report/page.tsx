"use client";

import { useParams } from "next/navigation";

import { Card } from "@/components/ui/card";

import {
  useScanResults,
} from "@/hooks/use-scan-results";

export default function ReportPage() {
  const params = useParams();

  const scanId =
    params.id as string;

  const {
    data,
    isLoading,
    error,
  } = useScanResults(scanId);

  if (isLoading) {
    return (
      <div className="p-6">
        Loading report...
      </div>
    );
  }

  if (error) {
    console.error(error);

    return (
      <div className="p-6">
        Failed to load report
      </div>
    );
  }

  const report = data?.data;

  return (
    <div className="mx-auto max-w-4xl p-6">
      <h1 className="mb-6 text-4xl font-bold">
        API Health Report
      </h1>

      <Card className="mb-6 p-6">
        <h2 className="text-2xl font-semibold">
          Health Score
        </h2>

        <p className="mt-4 text-5xl font-bold">
          {report?.health_score}/100
        </p>
      </Card>

      <Card className="mb-6 p-6">
        <h2 className="mb-4 text-xl font-semibold">
          Performance
        </h2>

        <div className="space-y-2">
          <p>
            Average Latency:
            {" "}
            {
              report?.performance
                .average_latency_ms
            }
            ms
          </p>

          <p>
            Minimum Latency:
            {" "}
            {
              report?.performance
                .min_latency_ms
            }
            ms
          </p>

          <p>
            Maximum Latency:
            {" "}
            {
              report?.performance
                .max_latency_ms
            }
            ms
          </p>

          <p>
            P95 Latency:
            {" "}
            {
              report?.performance
                .p95_latency_ms
            }
            ms
          </p>
        </div>
      </Card>

      <Card className="mb-6 p-6">
        <h2 className="mb-4 text-xl font-semibold">
          Availability
        </h2>

        <div className="space-y-2">
          <p>
            Success Rate:
            {" "}
            {
              report?.availability
                .success_rate
            }
            %
          </p>

          <p>
            Successful Requests:
            {" "}
            {
              report?.availability
                .successful_requests
            }
          </p>

          <p>
            Failed Requests:
            {" "}
            {
              report?.availability
                .failed_requests
            }
          </p>
        </div>
      </Card>

      <Card className="mb-6 p-6">
        <h2 className="mb-4 text-xl font-semibold">
          Rate Limiting
        </h2>

        <div className="space-y-2">
          <p>
            Detected:
            {" "}
            {
              report?.rate_limiting
                .detected
                ? "Yes"
                : "No"
            }
          </p>

          <p>
            Total Requests:
            {" "}
            {
              report?.rate_limiting
                .total_requests
            }
          </p>

          <p>
            Rate Limited Requests:
            {" "}
            {
              report?.rate_limiting
                .rate_limited_requests
            }
          </p>
        </div>
      </Card>

      <Card className="mb-6 p-6">
        <h2 className="mb-4 text-xl font-semibold">
          Security
        </h2>

        <div className="space-y-2">
          <p>
            HTTPS Enabled:
            {" "}
            {
              report?.security
                .https_enabled
                ? "Yes"
                : "No"
            }
          </p>

          <p>
            HSTS:
            {" "}
            {
              report?.security
                .headers.hsts
                ? "Yes"
                : "No"
            }
          </p>

          <p>
            X-Frame-Options:
            {" "}
            {
              report?.security
                .headers
                .x_frame_options
                ? "Yes"
                : "No"
            }
          </p>

          <p>
            X-Content-Type-Options:
            {" "}
            {
              report?.security
                .headers
                .x_content_type_options
                ? "Yes"
                : "No"
            }
          </p>
        </div>
      </Card>

      <Card className="p-6">
        <h2 className="mb-4 text-xl font-semibold">
          Error Handling
        </h2>

        <p>
          Proper 404:
          {" "}
          {
            report?.error_handling
              .proper_404
              ? "Yes"
              : "No"
          }
        </p>
      </Card>
    </div>
  );
}