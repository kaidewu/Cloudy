export interface Error {
    status: number
    errorId: string
    errorLevel: string
    errorMessage: string
}

export interface ErrorResponse {
    detail: Error[]
}