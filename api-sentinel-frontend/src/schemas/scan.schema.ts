import {z} from "zod";

export const CreateScanSchema = z.object({
    base_url : z.string().url().max(2048),
})

export const CreateScanResponseSchema = z.object({
    success : z.boolean(),

    data : z.object({
        scan_id : z.string(),
        status : z.enum([
            "queued",
            "running",
            "completed",
            "failed",
        ]),
        created_at :z.string(),
    }),
});