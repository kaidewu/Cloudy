'use client'

import { useEffect, useState } from "react"
import { Error } from "@/types/error"
import { UserResponse } from "@/types/user"
import { UserRolesResponse } from "@/types/user"
import Alerts from "@/components/Alerts"
import Loading from "@/components/Loading"
import Dropdown from "@/components/Users/Dropdown"

function Users() {
    const [isLoading, setLoading] = useState(false)
    const [error, setError] = useState<Error | null>(null)
    const [users, setUsers] = useState<UserResponse | null>(null)
    const [roles, setRoles] = useState<UserRolesResponse | null>(null)

    async function GetUsers(endpoint: string) {

        try{
            const response = await fetch(endpoint)
            const data = await response.json()
            if (!response.ok){
                setError(data)
            } else {
                setUsers(data)
            }
        } catch (error){
            console.error('Error fetching data:', error)
        } finally {
            setLoading(false)
        }
    }

    async function GetRoles(endpoint: string) {

        try{
            const response = await fetch(endpoint)
            const data = await response.json()
            if (!response.ok){
                setError(data)
            } else {
                setRoles(data)
            }
        } catch (error){
            console.error('Error fetching data:', error)
        } finally {
            setLoading(false)
        }
    }

    useEffect(() => {
        // Set Loading to True
        setLoading(true)
        GetRoles(process.env.NEXT_PUBLIC_API_ENDPOINT + "/user/roles" || "")
        GetUsers(process.env.NEXT_PUBLIC_API_ENDPOINT + "/users" || "")
    }, [])

    return(
        <>
            {isLoading ? (
                <Loading />
            ): error ? (
                <Alerts errorData={error}/>
            ): (
                <div>
                    <table className="min-w-full divide-y divide-gray-200">
                        <thead>
                            <tr>
                                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
                                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Role</th>
                                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Action</th>
                            </tr>
                        </thead>
                        <tbody className="bg-white divide-y divide-gray-200">
                            {users?.users?.map((user) => (
                                <tr key={user?.userId}>
                                    <td className="px-6 py-4 whitespace-nowrap">{user?.userName}</td>
                                    <td className="px-6 py-4 whitespace-nowrap">{user?.userMail}</td>
                                    <td className="px-6 py-4 whitespace-nowrap">
                                        <Dropdown actualUserRole={user?.userRoleName} userRoles={roles?.userRoles}/>
                                    </td>
                                    <td className="px-6 py-4 whitespace-nowrap">
                                        <span 
                                        className= {`${user?.userActive ?
                                            'px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800':
                                            'px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800'}`}>
                                            {`${user?.userActive ? 'Active': 'Inactive'}`}
                                        </span>
                                    </td>
                                    <td className="px-6 py-4 whitespace-nowrap">
                                        <button className="px-4 py-2 font-medium text-white bg-blue-600 rounded-md hover:bg-blue-500 focus:outline-none focus:shadow-outline-blue active:bg-blue-600 transition duration-150 ease-in-out">Edit</button>
                                        <button className="ml-2 px-4 py-2 font-medium text-white bg-red-600 rounded-md hover:bg-red-500 focus:outline-none focus:shadow-outline-red active:bg-red-600 transition duration-150 ease-in-out">Delete</button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </>
    )
}

export default Users