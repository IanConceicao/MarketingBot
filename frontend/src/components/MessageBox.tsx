import { getBackendUrl } from "../Api"
import type { Message } from "../types/Message"

import ActionBox from "./ActionBox"

interface MessageBoxProps {
  message: Message
  userId: string
  validAction: boolean
  fetchMessages: () => void
}

export default function MessageBox({
  message,
  userId,
  validAction,
  fetchMessages,
}: MessageBoxProps) {
  const backendUrl = getBackendUrl()
  return (
    <div className="gap-y-1 flex flex-col max-w-[80%]">
      <div className="w-fit rounded-xl px-4 py-2 text-white bg-green-400 shadow-sm">
        {message.imageUrl !== null && message.imageUrl.trim() !== "" && (
          <div className="py-2">
            <img
              alt="Ad"
              src={backendUrl + message.imageUrl.substring(1)}
              className="rounded-lg"
            />
          </div>
        )}
        {message.text}
      </div>

      {message.actions.map((action) => (
        <ActionBox
          key={action.id}
          action={action}
          userId={userId}
          fetchMessages={fetchMessages}
          validAction={validAction}
        />
      ))}
      <div></div>
    </div>
  )
}
