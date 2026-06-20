"use client"

import {useForm} from "react-hook-form"
import { useRouter } from "next/navigation";
import {zodResolver} from "@hookform/resolvers/zod"
import {z} from "zod"
import { CreateScanSchema } from "@/schemas/scan.schema";
import { useCreateScan } from "@/hooks/use-create-scan";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card } from "@/components/ui/card";

type FormValues = z.infer<typeof CreateScanSchema>;


export default function NewScanPage(){
    const router = useRouter()
    const createScanMutation = useCreateScan();
    const form = useForm<FormValues>({
        resolver : zodResolver(
            CreateScanSchema
        ),
        defaultValues: {
            base_url: "",
        },
    })

    const onSubmit = (
        values: FormValues
        ) => {
        console.log("SUBMITTED", values)
        createScanMutation.mutate(
            values,
            {
            onSuccess: (response) => {
              console.log("SUCCESS", response);
                router.push(
                `/scans/${response.data.scan_id}`
                );
            },

            onError: (error) => {
            console.log("ERROR", error);}
            }
        );
    }
    return (
  <div className="flex min-h-screen items-center justify-center p-6">
    <Card className="w-full max-w-md p-6">
      <h1 className="text-2xl font-bold">
        API Sentinel
      </h1>

      <p className="mt-2 mb-6 text-sm text-muted-foreground">
        Analyze your API health
      </p>

      <form
        onSubmit={form.handleSubmit(
          onSubmit
        )}
        className="space-y-4"
      >
        <Input
          placeholder="https://api.example.com"
          {...form.register(
            "base_url"
          )}
        />

        {form.formState.errors
          .base_url && (
          <p className="text-sm text-red-500">
            {
              form.formState.errors
                .base_url.message
            }
          </p>
        )}

        <Button
          type="submit"
          className="w-full"
          disabled={
            createScanMutation.isPending
          }
        >
          {createScanMutation.isPending
            ? "Starting Scan..."
            : "Start Scan"}
        </Button>
      </form>
    </Card>
  </div>
);
}
    