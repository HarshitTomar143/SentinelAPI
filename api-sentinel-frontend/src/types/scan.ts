export type ScanStatus = 
| "queued"
| "running"
| "completed"
| "failed";

export interface CreateScanRequest {
    base_url : string;
}

export interface CreateScanResponse {
    success : boolean;

    data :{
        scan_id : string ;
        status : ScanStatus;
        created_at : string;
    };
}