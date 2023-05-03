export interface Message {
  id: number
  imageUrl: string | null
  impressionCount: number
  text: string
  actions: Action[]
}
