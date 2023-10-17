export interface User{
    userId: number
    userName: string
    userSurname: string
    userCreateAt: string
    userLogin: string
    userMail: string
    userPhone: string
    userBirthdate: string
    userLastLogin: string
    userActive: boolean
}

export interface UserResponse {
    status: number
    users: User[]
}