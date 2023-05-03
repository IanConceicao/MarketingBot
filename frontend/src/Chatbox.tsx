import { useEffect, useRef, useState } from "react"

import { getMessagesForUser, recordImpression } from "./Api"
import MessageBox from "./components/MessageBox"
import SelectUser from "./components/SelectUser"
import type { Message } from "./types/Message"

export default function Chatbox() {
  const messagesEndRef = useRef<null | HTMLDivElement>(null)
  const [userId, setUserId] = useState("Ian")
  const [messages, setMessages] = useState<Message[]>([])

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }

  const fetchTheMessages = async () => {
    setMessages(await getMessagesForUser(userId))
  }

  useEffect(() => {
    fetchTheMessages()
  }, [userId])

  useEffect(() => {
    scrollToBottom()
    messages.forEach((message) => recordImpression(userId, message.id))
  }, [messages])

  return (
    <div className="column gap-y-4 flex flex-col items-center justify-center w-screen h-screen">
      <div className="w-96 h-[38rem] bg-slate-50 rounded-2xl shadow-2xl ">
        <div className="flex flex-col justify-between h-full">
          <div className="basis-16 bg-slate-100 shrink-0 rounded-t-2xl flex flex-col justify-center w-full">
            <div className="text-slate-700 font-sans text-2xl text-center">
              Marketing Bot
            </div>
          </div>
          <div className="gap-y-4 grow flex flex-col w-full p-4 overflow-scroll">
            {messages.map((message, index) => (
              <MessageBox
                key={message.text}
                message={message}
                userId={userId}
                fetchMessages={fetchTheMessages}
                validAction={index == messages.length - 1}
              />
            ))}
            <div ref={messagesEndRef} />
          </div>
          <div className="basis-20 bg-slate-100 shrink-0 rounded-b-2xl flex flex-col justify-center w-full py-4">
            <input
              type="text"
              className="form-input grow rounded-2xl shrink-0 border-slate-100 mx-10 border-none"
            />
          </div>
        </div>
      </div>
      <SelectUser setUserId={setUserId} userId={userId} />
    </div>
  )
}
