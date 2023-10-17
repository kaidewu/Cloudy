import { useEffect, useState } from 'react'

const Alerts = ({errorData}) => {
    const [visible, setVisible] = useState(true)

    useEffect(() => {
        const timeout = setTimeout(() => {
            setVisible(false)
        }, 8000)

        return () => clearTimeout(timeout)
    }, []);

    if (!visible) {
        return null
    }

    return (
        <div>
            {(errorData?.status >= 500 && errorData?.status <= 509) ? (
                /* Danger */
                <div className="px-8 py-6 bg-red-400 text-white flex justify-between rounded">
                    <div className="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-7 w-7 mr-6" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                </svg>
                        <p>{errorData?.errorId}</p>
                    </div>
                    <button className="text-red-100 hover:text-white">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>
            ): (
                /* Warning */
                <div className="px-8 py-6 bg-yellow-400 text-white flex justify-between rounded">
                    <div className="flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-7 w-7 mr-6" viewBox="0 0 20 20" fill="currentColor">
                <path d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z" />
                </svg>
                        <p>{errorData?.errorId}</p>
                    </div>
                    <button className="text-yellow-100 hover:text-white">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>
            )}
        </div>
    )
}

export default Alerts
