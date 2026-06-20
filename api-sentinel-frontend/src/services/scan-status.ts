import {api} from "@/lib/api";

import{
    ScanStatusSchema,
} from "@/schemas/scan-status.schema";


export const getScanStatus = async(scanId: string) => {
    const response = await api.get( `/api/v1/scans/${scanId}`);
    return ScanStatusSchema.parse(response.data)
}