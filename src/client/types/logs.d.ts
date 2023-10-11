export interface Logs {
    status: number
    logs: {
        logId: string
        logRegisterAt: string
        logTitle: string
        logBody: string
        logEndpoint: string
        logLevel: string
    }
}