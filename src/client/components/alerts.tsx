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
                <div className="px-8 py-6 bg-yellow-400 text-white flex justify-between rounded-lg w-1/3 mt-10 ml-10">
                    <div className="flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        <span className="px-3">{errorData?.errorId}</span>
                    </div>
                </div>
            ): (
                /* Warning */
                <div className="px-8 py-6 bg-yellow-400 text-white flex justify-between rounded-lg w-1/3 mt-10 ml-10">
                    <div className="flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                        </svg>
                        <span className="px-3">{errorData?.errorId}</span>
                    </div>
                </div>
            )}
        </div>
    )
}

export default Alerts