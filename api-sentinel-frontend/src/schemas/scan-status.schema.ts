import {z} from "zod"

export const ScanStatusSchema = z.object({
    success : z.boolean(),
    data : z.object({
        scan_id : z.string(),
        status  : z.enum([
            "queued",
            "running",
            "finished",
            "failed",
        ]),

        progress: z.number(),
        current_stage: z.string()
    }),
});

export type ScanStatusResponse = z.infer<typeof ScanStatusSchema>