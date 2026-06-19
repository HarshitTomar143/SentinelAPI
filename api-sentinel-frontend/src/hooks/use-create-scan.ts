import {useMutation} from "@tanstack/react-query";
import {createScan} from "@/services/scan";

export const useCreateScan = () => {
    return useMutation({
        mutationFn: createScan,
    })
}