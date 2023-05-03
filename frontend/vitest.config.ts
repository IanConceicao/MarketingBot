import EnvironmentPlugin from "vite-plugin-environment"
import { defineConfig } from "vitest/config"
export default defineConfig({
  plugins: [EnvironmentPlugin(["BACKEND_URL"])],
  test: {
    environment: "jsdom",
    globals: true,
    setupFiles: ["./src/setupTests.ts"],
  },
})
