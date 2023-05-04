export interface Action {
  id: number
  text: string
  prompt: number
  nextPrompt: number | null
  redirect: string
  clickEventCount: number
}
