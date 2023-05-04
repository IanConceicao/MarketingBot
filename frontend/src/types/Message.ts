import type { Action } from "./Action"
import type { Prompt } from "./Prompt"

export interface Message {
  id: number
  prompt: Prompt
  actions: Action[]
}
