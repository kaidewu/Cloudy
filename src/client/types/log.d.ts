export interface Log {
    logId: string
    logRegisterAt: string
    logTitle: string
    logBody: string
    logEndpoint: string
    logLevel: number
  }
  
  export interface LogsResponse {
    status: number
    logs: Log[]
  }