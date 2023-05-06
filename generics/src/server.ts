import express, { Request, Response } from "express";

// Define a generic response type
interface APIResponse<T> {
  success: boolean;
  data: T;
}

const app = express();
app.use(express.json());

// Generic endpoint for numbers
app.get("/api/number/:value", (req: Request, res: Response) => {
  const value: number = parseInt(req.params.value);
  const response: APIResponse<number> = {
    success: true,
    data: value,
  };
  res.json(response);
});

// Generic endpoint for strings
app.get("/api/string/:value", (req: Request, res: Response) => {
  const value: string = req.params.value;
  const response: APIResponse<string> = {
    success: true,
    data: value,
  };
  res.json(response);
});

app.listen(3000, () => {
  console.log("Server is listening on port 3000");
});
