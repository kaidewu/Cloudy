import { useEffect, useRef, useState } from 'react'

const Dropdown = ({ userRoles, actualUserRole }) => {
    const [isOpen, setIsOpen] = useState<boolean>(false)
    const dropdownRef = useRef<HTMLDivElement | null>(null)
  
    const toggleDropdown = () => {
      setIsOpen(!isOpen)
    }
  
    const closeDropdown = () => {
      setIsOpen(false)
    }
  
    useEffect(() => {
      function handleClickOutside(event: MouseEvent) {
        if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
          closeDropdown()
        }
      }
  
      if (isOpen) {
        document.addEventListener('mousedown', handleClickOutside)
      } else {
        document.removeEventListener('mousedown', handleClickOutside)
      }
  
      return () => {
        document.removeEventListener('mousedown', handleClickOutside)
      }
    }, [isOpen])

    return (
        <div className="relative inline-block text-left z-99">
            <button
                className="bg-primary text-black uppercase py-2 px-4 rounded shadow hover:bg-primary-600 focus:outline-none"
                onClick={toggleDropdown}
            >
                {actualUserRole}
            </button>
            <div
                className={`origin-top-right absolute right-0 mt-2 w-40 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 ${
                isOpen ? '' : 'hidden'
                }`}
            >
                <ul className="py-1">
                {userRoles.map((role) => (
                    <li key={role.userRolId}>
                    <button
                        className={`${
                        role.userRolName !== actualUserRole
                            ? 'text-gray-700 hover:bg-gray-100'
                            : 'text-gray-400 pointer-events-none'
                        } block px-4 py-2 text-sm text-left w-full`}
                        onClick={toggleDropdown}
                    >
                        {role.userRolName}
                    </button>
                    </li>
                ))}
                </ul>
            </div>
        </div>
    )
}

export default Dropdown