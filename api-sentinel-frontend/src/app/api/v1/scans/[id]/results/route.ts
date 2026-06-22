import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({
    success: true,

    data: {
      scan_id: "demo",

      health_score: 84,

      performance: {
        average_latency_ms: 120,
        min_latency_ms: 80,
        max_latency_ms: 450,
        p95_latency_ms: 210,
      },

      availability: {
        success_rate: 98,
        successful_requests: 98,
        failed_requests: 2,
      },

      rate_limiting: {
        detected: true,
        total_requests: 100,
        rate_limited_requests: 14,
      },

      security: {
        https_enabled: true,

        headers: {
          hsts: true,
          x_frame_options: false,
          x_content_type_options: true,
        },
      },

      error_handling: {
        proper_404: true,
      },
    },
  });
}