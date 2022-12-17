import { readLines } from "https://deno.land/std@0.168.0/io/mod.ts";

async function main() {
  const filename = "input.txt";
  const file = await Deno.open(filename);
  for await (const line of readLines(file)) {
    console.log(line);
  }
}

await main();
