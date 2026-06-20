import { NextResponse } from "next/server";


export async function GET(){
    return NextResponse.json({
        success: true,
        data: {
            scan_id : crypto.randomUUID(),
            status: "running",
            progress: 60,
            current_state: "rate-limit-scan"
        },
    });
}