import {z} from "zod"

const PerformanceSchema = 
    z.object({
        average_latesncy_ms : z.number(),
        min_latency_ms: z.number(),
        max_latency_ms: z.number(),
        p95_latency_ms: z.number(), 
    })

const AvailabilitySchema = 
    z.object({
        success_rate : z.number(),
        successful_requests : z.number(),
        failed_requests: z.number(),
    });

const RateLimitingSchema = 
    z.object({
        detected: z.boolean(),
        total_request : z.number(),
        rate_limited_requests: z.number(),
    });

const SecurityHeadersSchema = 
    z.object({
        hsts: z.boolean(),
        x_frame_options: z.boolean(),
        x_content_type_options: z.boolean(),
    });
    
const SecuritySchema = 
    z.object({
        https_enabled: z.boolean(),
        headers: SecurityHeadersSchema,
    });    

const ErrorHandlingSchema = 
    z.object({
        proper_404 : z.boolean(),
    })    

export const ScanResultSchema = 
    z.object({
        success: z.boolean(),
        data: z.object({
            scan_id : z.string(),
            health_score : z.number(),
            performance : PerformanceSchema,
            availability : AvailabilitySchema,
            rate_limiting: RateLimitingSchema,
            security : SecuritySchema,
            error_handling : ErrorHandlingSchema,
        }),
    });

export type ScanResultSchema = z.infer<typeof ScanResultSchema>;    