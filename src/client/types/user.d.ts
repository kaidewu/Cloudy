export interface User{
    userId: number
    userName: string
    userSurname: string
    userCreateAt: string
    userLogin: string
    userMail: string
    userPhone: string
    userBirthdate: string
    userRoleId: number
    userRoleName: string
    userLastLogin: string
    userActive: boolean
}

export interface UserResponse {
    status: number
    users: User[]
}

export interface UserRoles {
    userRolId: number
    userRolName: string
}

export interface UserRolesResponse {
    status: number
    userRoles: UserRoles[]
}