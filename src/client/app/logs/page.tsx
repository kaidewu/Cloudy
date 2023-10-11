'use client'

import { Logs } from '@/types/logs'
import { Error } from '@/types/error'
import { useState, useEffect } from 'react'
import Alerts from '@/components/alerts'

function Logs() {
  const [logs, setLogs] = useState<Logs | null>(null)
  const [error, setError] = useState<Error | null>(null)

  useEffect(() => {
    fetch("http://192.168.1.47/api/v1/user/1/wallet")
      .then(async (response) => (response.json()))
      .then((data) => {
        if (data?.status === 200) {
            setLogs(data)
        } else {
            setError(data)
        }
      })
      .catch((err) => {
        console.error(err.massage)
      })
  }, [])

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
        {error?.status === 500 ? (
            <Alerts errorData={error} />
        ): error?.status === 400 ? (
            <Alerts errorData={error} />
        ): logs?.status === 200 ? (
            <code className="font-mono font-bold">{logs ? JSON.stringify(logs) : null}</code>
        ): null}
    </main>
  )
}


export default Logs