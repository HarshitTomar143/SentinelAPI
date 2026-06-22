import {api} from "@/lib/api"

import {
    ScanResultsSchema,
}from "@/schemas/scan-results.schema";

export const getScanResults = async(scanId: string) => {
    const response = await api.get(
         `/api/v1/scans/${scanId}/results`
    );

    return ScanResultsSchema.parse(
        response.data
    )
}