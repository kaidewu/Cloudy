'use client'

import { LogsResponse } from '@/types/logs'
import { Error } from '@/types/error'
import React, { useState, useEffect } from 'react'
import Alerts from '@/components/Alerts'
import Loading from '@/components/Loading'
import Filters from '@/components/Logs/Filters'

const Logs: React.FC = () => {
  const [logs, setLogs] = useState<LogsResponse | null>(null)
  const [error, setError] = useState<Error | null>(null)
  const [isLoading, setLoading] = useState(false)
  const [currentPage, setCurrentPage] = useState(1)
  const itemsPerPage = 15
  const indexOfLastItem = currentPage * itemsPerPage
  const indexOfFirstItem = indexOfLastItem - itemsPerPage

  async function GetLogs(Endpoint: string) {

    setLoading(true)

    try {
      const response = await fetch(Endpoint)
      if (!response.ok) {
        const error = await response.json()
        setError(error)
      } else {
        const data = await response.json()
        setLogs(data)
      }
    } catch (error) {
      console.error('Error fetching data:', error)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    // Make the initial API call when the component mounts
    GetLogs(process.env.NEXT_PUBLIC_API_ENDPOINT + "/logs" || "")
  }, [])

  const currentItems = logs?.logs?.slice(indexOfFirstItem, indexOfLastItem)
  const totalPages = Math.ceil((logs?.logs?.length || 0) / itemsPerPage)

  const getPageNumbers = () => {
    const pageNumbers = []
    for (let i = 1; i <= totalPages; i++) {
      pageNumbers.push(i)
    }
    return pageNumbers
  }

  const renderPageNumbers = () => {
    if (totalPages <= 5) {
      return getPageNumbers().map((number) => (
        <li key={number}>
          <button
            className={`${number === currentPage ? 
              'flex items-center justify-center px-4 h-10 text-blue-600 border border-gray-300 bg-blue-50 hover:bg-blue-100 hover:text-blue-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white' : 
              'flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'}`}
            onClick={() => setCurrentPage(number)}
          >
            {number}
          </button>
        </li>
      ));
    } else {
      const visiblePages = 5
      const halfVisiblePages = Math.floor(visiblePages / 2)
      const startPage = Math.max(1, currentPage - halfVisiblePages)
      const endPage = Math.min(totalPages, startPage + visiblePages - 1)
      const items = []
      if (startPage > 1) {
        items.push(
          <li key={1}>
            <button
              className="flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
              onClick={() => setCurrentPage(1)}
            >
              1
            </button>
          </li>
        )
        if (startPage > 2) {
          items.push(
          <li key="ellipsis-start">
            <button
              className="flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                ...
              </button>
          </li>
          )
        }
      }
      for (let i = startPage; i <= endPage; i++) {
        items.push(
          <li key={i}>
            <button
              className={`${i === currentPage ? 
                'flex items-center justify-center px-4 h-10 text-blue-600 border border-gray-300 bg-blue-50 hover:bg-blue-100 hover:text-blue-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white' : 
                'flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white'}`}
              onClick={() => setCurrentPage(i)}
            >
              {i}
            </button>
          </li>
        )
      }
      if (endPage < totalPages) {
        if (endPage < totalPages - 1) {
          items.push(<li key="ellipsis-start">
          <button
            className="flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
              ...
            </button>
        </li>)
        }
        items.push(
          <li key={totalPages}>
            <button
              className="flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
              onClick={() => setCurrentPage(totalPages)}
            >
              {totalPages}
            </button>
          </li>
        )
      }
      return items;
    }
  }

  return (
    <>
      { isLoading ? (
        <div id="Loading">
          <Loading />
        </div>
      ): error ? (
        <div id="Error Alert">
          <Alerts errorData={error} />
        </div>
      ) : (
      <div className="min-h-screen bg-gray-100 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
        <div className="overflow-x-auto">
          <table className="w-full bg-white border border-gray-300">
            <thead>
              <tr>
                <th className="px-6 py-3 border-b border-gray-300 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Logs</th>
              </tr>
            </thead>
            <tbody>
            {currentItems?.map((log) => (
              <tr key={log?.logId}>
                <td className="px-6 py-4 border-b border-gray-300">
                  <details>
                    <summary className="cursor-pointer">
                      {log?.logRegisterAt} - {log?.logId}
                      <br/>
                      <span className="cursor-pointer font-bold text-blue-400 text-sm">
                        {log?.logTitle}
                      </span>
                    </summary>
                    <div className="LogDescriptions">
                      <div id="LogLevel" className="mt-5">
                        <p className="font-bold">level</p>
                        <div className="px-4 py-2 whitespace-pre-line text-justify">
                          <p>
                            {log?.logLevel}
                          </p>
                        </div>
                      </div>
                      <div id="LogMessages" className="mt-5">
                        <p className="font-bold">message</p>
                        <div className="px-4 py-2 bg-gray-200 whitespace-pre-line text-justify">
                          <code>
                            {log?.logBody}
                          </code>
                        </div>
                      </div>
                      <div id="LogSource" className="mt-5">
                        <p className="font-bold">source</p>
                        <div className="px-4 py-2 whitespace-pre-line text-justify">
                          <p>
                            {log?.logEndpoint}
                          </p>
                        </div>
                      </div>
                      <div id="LogTimestamp" className="mt-5">
                        <p className="font-bold">timestamp</p>
                        <div className="px-4 py-2 whitespace-pre-line text-justify">
                          <p>
                            {log?.logRegisterAt}
                          </p>
                        </div>
                      </div>
                    </div>
                  </details>
                </td>
              </tr>
            ))}
            </tbody>
          </table>
          <div className="pagination-container">
            <nav aria-label="Page navigation" className="items-center">
              <ul className="inline-flex -space-x-px text-base h-10">
                <li>
                  <button
                    className="flex items-center justify-center px-4 h-10 ml-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-l-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
                    onClick={() => setCurrentPage(currentPage - 1)}
                    disabled={currentPage === 1}
                  >
                    Previous
                  </button>
                </li>
                {renderPageNumbers()}
                <li>
                  <button
                    className="flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 rounded-r-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
                    onClick={() => setCurrentPage(currentPage + 1)}
                    disabled={currentPage === totalPages}
                  >
                    Next
                  </button>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
      )}
    </>
  )
}


export default Logs