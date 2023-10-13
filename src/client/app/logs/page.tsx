'use client'

import { LogsResponse } from '@/types/logs'
import { Error } from '@/types/error'
import { useState, useEffect } from 'react'
import Alerts from '@/components/alerts'
import Table from '@/components/Table'
import Loading from '@/components/Loading'

const Logs = () => {
  const [logs, setLogs] = useState<LogsResponse | null>(null)
  const [error, setError] = useState<Error | null>(null)
  const [isLoading, setLoading] = useState(false)

  function GetLogs(errorId: string) {

    setLoading(true)

    fetch("http://192.168.1.47/api/v1/logs?errorId=" + errorId)
      .then(async (response) => {
        const data = await response.json()

        if (data?.status >= 400 && data?.status <= 509) {
          setError(data)
          return
        } else {
          setLogs(data?.logs)
        }
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      })
      .finally(() => {
        // set loading to false after everything has completed.
        setLoading(false)
      })
  }
  
  useEffect(() => {
    // Make the initial API call when the component mounts
    GetLogs("")
  }, [])

  return (
    <>
      { isLoading ? (
        <Loading />
      ): error ? (
        <Alerts errorData={error} />
      ) : (
        <Table data={logs} />
      )}
    </>
  )
}


export default Logs