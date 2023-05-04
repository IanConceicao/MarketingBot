import type { ChangeEvent } from "react"
import { useEffect, useState } from "react"

import { getAllUsers } from "../Api"

interface NavbarProps {
  userId: string
  setUserId: (userId: string) => void
}

export default function SelectUser({ userId, setUserId }: NavbarProps) {
  const [allUserIds, setAllUserIds] = useState([userId])
  const [selectedUserId, setSelectedUserId] = useState(userId)

  useEffect(() => {
    const fetchUserIds = async () => {
      setAllUserIds(await getAllUsers())
    }

    fetchUserIds()
  }, [])

  const handleChange = (e: ChangeEvent<HTMLSelectElement>) => {
    const newName = e.target.value
    setSelectedUserId(newName)
    setUserId(newName)
  }

  return (
    <select
      value={selectedUserId}
      onChange={handleChange}
      className="rounded-3xl w-36 px-5 bg-white shadow-lg"
    >
      {allUserIds.map((userId) => (
        <option key={userId} value={userId}>
          {userId}
        </option>
      ))}
    </select>
  )
}
