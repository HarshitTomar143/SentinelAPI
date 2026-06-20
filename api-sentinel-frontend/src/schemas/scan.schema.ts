import {z} from "zod";

export const CreateScanSchema = z.object({
    base_url : z.string()
    .min(1, "Base URL is required")
    .url("Please enter a valid url")
    .max(2048, "URL is too long"),
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