'use client'

import { Log, LogsResponse } from '@/types/logs'
import { useState, useEffect } from 'react'
import Alerts from '@/components/alerts'

function LogsPage() {
  const [logs, setLogs] = useState<Log[]>([])
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetch("http://192.168.1.47/api/v1/logs")
      .then(async (response) => {
        if (!response.ok) {
          const errorData: LogsResponse = await response.json()
          setError(errorData?.status.toString())
          return
        }
        return response.json()
      })
      .then((data: LogsResponse) => {
        setLogs(data.logs)
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
        setError('500')
      })
  }, [])

  return (
    <main>
      {error ? (
        <Alerts errorData={error} />
      ) : (
        <div className="container w-full md:w-4/5 xl:w-3/5 mx-auto px-2">
          <div
            id='recipients'
            className="p-8 mt-6 lg:mt-0 rounded shadow bg-white text-black"
          >
            <table
              id="example"
              className="stripe hover"
              style={{ width: "100%", paddingTop: "1em", paddingBottom: "1em" }}
            >
              {/* Table headers */}
              <thead>
                <tr>
                  <th data-priority="1">Id</th>
                  <th data-priority="2">Title</th>
                  <th data-priority="3">Type</th>
                  <th data-priority="4">Enpoint</th>
                  <th data-priority="5">Traceback</th>
                  <th data-priority="6">Register At</th>
                </tr>
              </thead>
              {/* Table body */}
              <tbody>
                {logs?.map((log, index) => (
                  <tr key={index}>
                    <td>{log?.logId}</td>
                    <td>{log?.logTitle}</td>
                    <td>{log?.logLevel}</td>
                    <td>{log?.logEndpoint}</td>
                    <td>{log?.logBody}</td>
                    <td>{log?.logRegisterAt}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </main>
  )
}


export default LogsPage