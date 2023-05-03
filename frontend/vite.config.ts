import react from "@vitejs/plugin-react-swc"
import { defineConfig } from "vite"
import EnvironmentPlugin from "vite-plugin-environment"

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    sourcemap: true,
  },
  plugins: [react(), EnvironmentPlugin(["BACKEND_URL"])],
  publicDir: "public",
  server: {
    host: true,
    port: 3000,
  },
})
