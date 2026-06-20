import { NextResponse } from "next/server";



export async function POST(){
    await new Promise((resolve)=>{
        setTimeout(resolve,1500)
    });
    return NextResponse.json({
        success: true,

        data : {
            scan_id: crypto.randomUUID(),
            status: "queued",
            created_at : new Date().toISOString(),
        }
    })
}