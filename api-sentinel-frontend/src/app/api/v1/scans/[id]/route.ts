import { NextResponse } from "next/server";

const scanProgress =
  new Map<string, number>();

export async function GET(
  request: Request,
  {
    params,
  }: {
    params: Promise<{ id: string }>;
  }
) {
  const { id } = await params;

  const currentProgress =
    scanProgress.get(id) ?? 0;

  const newProgress =
    Math.min(
      currentProgress + 20,
      100
    );

  scanProgress.set(
    id,
    newProgress
  );

  return NextResponse.json({
    success: true,

    data: {
      scan_id: id,

      status:
        newProgress === 100
          ? "completed"
          : "running",

      progress: newProgress,

      current_stage:
        newProgress === 100
          ? "report_generation"
          : "rate_limit_scan",
    },
  });
}