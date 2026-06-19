import { CreateScanResponseSchema } from "@/schemas/scan.schema";
import { CreateScanRequest } from "@/types/scan";
import { api } from "@/lib/api";

export const createScan = async(payload: CreateScanRequest) => {
    const response  = await api.post(
        "/api/v1/scans", payload
    );

    return CreateScanResponseSchema.parse(
        response.data
    );
};