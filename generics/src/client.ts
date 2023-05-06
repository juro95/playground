import axios from "axios";

// Define a generic response type
interface APIResponse<T> {
  success: boolean;
  data: T;
}

async function main() {
  // Request number
  const numberResponse = await axios.get<APIResponse<number>>(
    "http://localhost:3000/api/number/42"
  );
  console.log("Number:", numberResponse.data.data);

  // Request string
  const stringResponse = await axios.get<APIResponse<string>>(
    "http://localhost:3000/api/string/hello"
  );
  console.log("String:", stringResponse.data.data);
}

main();
