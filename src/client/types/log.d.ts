export interface Log {
    logId: string
    logRegisterAt: string
    logTitle: string
    logBody: string
    logEndpoint: string
    logLevel: string
  }
  
  export interface LogsResponse {
    status: number
    logs: Log[]
  }