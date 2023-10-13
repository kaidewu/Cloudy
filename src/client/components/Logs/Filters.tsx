const Filters = () => {
    return (
        <div className="bg-gray-50">
            {/*
                Mobile filter dialog

                Off-canvas menu for mobile, show/hide based on off-canvas menu state.
            */}
            <div className="relative z-40 sm:hidden" role="dialog" aria-modal="true">
                {/*
                Off-canvas menu backdrop, show/hide based on off-canvas menu state.

                Entering: "transition-opacity ease-linear duration-300"
                    From: "opacity-0"
                    To: "opacity-100"
                Leaving: "transition-opacity ease-linear duration-300"
                    From: "opacity-100"
                    To: "opacity-0"
                */}
                <div className="fixed inset-0 bg-black bg-opacity-25"></div>

                <div className="fixed inset-0 z-40 flex">
                {/*
                    Off-canvas menu, show/hide based on off-canvas menu state.

                    Entering: "transition ease-in-out duration-300 transform"
                    From: "translate-x-full"
                    To: "translate-x-0"
                    Leaving: "transition ease-in-out duration-300 transform"
                    From: "translate-x-0"
                    To: "translate-x-full"
                */}
                <div className="relative ml-auto flex h-full w-full max-w-xs flex-col overflow-y-auto bg-white py-4 pb-6 shadow-xl">
                    <div className="flex items-center justify-between px-4">
                    <h2 className="text-lg font-medium text-gray-900">Filters</h2>
                    <button type="button" className="-mr-2 flex h-10 w-10 items-center justify-center rounded-md bg-white p-2 text-gray-400 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500">
                        <span className="sr-only">Close menu</span>
                        {/* Heroicon name: outline/x-mark */}
                        <svg className="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                    </div>

                    {/* Filters */}
                    <form className="mt-4">
                    <div className="border-t border-gray-200 px-4 py-6">
                        <h3 className="-mx-2 -my-3 flow-root">
                        {/* Expand/collapse question button */}
                        <button type="button" className="flex w-full items-center justify-between bg-white px-2 py-3 text-sm text-gray-400" aria-controls="filter-section-0" aria-expanded="false">
                            <span className="font-medium text-gray-900">Category</span>
                            <span className="ml-6 flex items-center">
                            {/*
                                Expand/collapse icon, toggle classes based on question open state.

                                Heroicon name: mini/chevron-down

                                Open: "-rotate-180", Closed: "rotate-0"
                            */}
                            <svg className="rotate-0 h-5 w-5 transform" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
                            </svg>
                            </span>
                        </button>
                        </h3>
                        <div className="pt-6" id="filter-section-0">
                        <div className="space-y-6">
                            <div className="flex items-center">
                            <input id="filter-mobile-category-0" name="category[]" value="tees" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-mobile-category-0" className="ml-3 text-sm text-gray-500">Tees</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-mobile-category-1" name="category[]" value="crewnecks" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-mobile-category-1" className="ml-3 text-sm text-gray-500">Crewnecks</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-mobile-category-2" name="category[]" value="hats" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-mobile-category-2" className="ml-3 text-sm text-gray-500">Hats</label>
                            </div>
                        </div>
                        </div>
                    </div>

                    <div className="border-t border-gray-200 px-4 py-6">
                        <h3 className="-mx-2 -my-3 flow-root">
                        {/* Expand/collapse question button */}
                        <button type="button" className="flex w-full items-center justify-between bg-white px-2 py-3 text-sm text-gray-400" aria-controls="filter-section-1" aria-expanded="false">
                            <span className="font-medium text-gray-900">Brand</span>
                            <span className="ml-6 flex items-center">
                            {/*
                                Expand/collapse icon, toggle classes based on question open state.

                                Heroicon name: mini/chevron-down

                                Open: "-rotate-180", Closed: "rotate-0"
                            */}
                            <svg className="rotate-0 h-5 w-5 transform" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
                            </svg>
                            </span>
                        </button>
                        </h3>
                        <div className="pt-6" id="filter-section-1">
                        <div className="space-y-6">
                            <div className="flex items-center">
                            <input id="filter-mobile-brand-0" name="brand[]" value="clothing-company" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-mobile-brand-0" className="ml-3 text-sm text-gray-500">Clothing Company</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-mobile-brand-1" name="brand[]" value="fashion-inc" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-mobile-brand-1" className="ml-3 text-sm text-gray-500">Fashion Inc.</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-mobile-brand-2" name="brand[]" value="shoes-n-more" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-mobile-brand-2" className="ml-3 text-sm text-gray-500">Shoes &#039;n More</label>
                            </div>
                        </div>
                        </div>
                    </div>

                    <div className="border-t border-gray-200 px-4 py-6">
                        <h3 className="-mx-2 -my-3 flow-root">
                        {/* Expand/collapse question button */}
                        <button type="button" className="flex w-full items-center justify-between bg-white px-2 py-3 text-sm text-gray-400" aria-controls="filter-section-2" aria-expanded="false">
                            <span className="font-medium text-gray-900">Color</span>
                            <span className="ml-6 flex items-center">
                            {/*
                                Expand/collapse icon, toggle classes based on question open state.

                                Heroicon name: mini/chevron-down

                                Open: "-rotate-180", Closed: "rotate-0"
                            */}
                            <svg className="rotate-0 h-5 w-5 transform" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
                            </svg>
                            </span>
                        </button>
                        </h3>
                        <div className="pt-6" id="filter-section-2">
                        <div className="space-y-6">
                            <div className="flex items-center">
                            <input id="filter-mobile-color-0" name="color[]" value="white" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-mobile-color-0" className="ml-3 text-sm text-gray-500">White</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-mobile-color-1" name="color[]" value="black" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-mobile-color-1" className="ml-3 text-sm text-gray-500">Black</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-mobile-color-2" name="color[]" value="grey" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-mobile-color-2" className="ml-3 text-sm text-gray-500">Grey</label>
                            </div>
                        </div>
                        </div>
                    </div>

                    <div className="border-t border-gray-200 px-4 py-6">
                        <h3 className="-mx-2 -my-3 flow-root">
                        {/* Expand/collapse question button */}
                        <button type="button" className="flex w-full items-center justify-between bg-white px-2 py-3 text-sm text-gray-400" aria-controls="filter-section-3" aria-expanded="false">
                            <span className="font-medium text-gray-900">Sizes</span>
                            <span className="ml-6 flex items-center">
                            {/*
                                Expand/collapse icon, toggle classes based on question open state.

                                Heroicon name: mini/chevron-down

                                Open: "-rotate-180", Closed: "rotate-0"
                            */}
                            <svg className="rotate-0 h-5 w-5 transform" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
                            </svg>
                            </span>
                        </button>
                        </h3>
                        <div className="pt-6" id="filter-section-3">
                        <div className="space-y-6">
                            <div className="flex items-center">
                            <input id="filter-mobile-sizes-0" name="sizes[]" value="s" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-mobile-sizes-0" className="ml-3 text-sm text-gray-500">S</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-mobile-sizes-1" name="sizes[]" value="m" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-mobile-sizes-1" className="ml-3 text-sm text-gray-500">M</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-mobile-sizes-2" name="sizes[]" value="l" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-mobile-sizes-2" className="ml-3 text-sm text-gray-500">L</label>
                            </div>
                        </div>
                        </div>
                    </div>
                    </form>
                </div>
                </div>
            </div>

            <div className="mx-auto max-w-3xl px-4 text-center sm:px-6 lg:max-w-7xl lg:px-8">

                <section aria-labelledby="filter-heading" className="border-t border-gray-200 py-6">
                <h2 id="filter-heading" className="sr-only">Product filters</h2>

                <div className="flex items-center justify-between">
                    <div className="relative inline-block text-left">
                    <div>
                        <button type="button" className="group inline-flex justify-center text-sm font-medium text-gray-700 hover:text-gray-900" id="mobile-menu-button" aria-expanded="false" aria-haspopup="true">
                        Sort
                        {/* Heroicon name: mini/chevron-down */}
                        <svg className="-mr-1 ml-1 h-5 w-5 flex-shrink-0 text-gray-400 group-hover:text-gray-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                            <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
                        </svg>
                        </button>
                    </div>

                    {/*
                        Dropdown menu, show/hide based on menu state.

                        Entering: "transition ease-out duration-100"
                        From: "transform opacity-0 scale-95"
                        To: "transform opacity-100 scale-100"
                        Leaving: "transition ease-in duration-75"
                        From: "transform opacity-100 scale-100"
                        To: "transform opacity-0 scale-95"
                    */}
                    <div className="absolute left-0 z-10 mt-2 w-40 origin-top-left rounded-md bg-white shadow-2xl ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="mobile-menu-button" tabIndex={-1}>
                        <div className="py-1" role="none">
                        {/* Active: "bg-gray-100", Not Active: "" */}
                        <a href="#" className="block px-4 py-2 text-sm font-medium text-gray-900" role="menuitem" tabIndex={-1} id="mobile-menu-item-0">Most Popular</a>

                        <a href="#" className="block px-4 py-2 text-sm font-medium text-gray-900" role="menuitem" tabIndex={-1} id="mobile-menu-item-1">Best Rating</a>

                        <a href="#" className="block px-4 py-2 text-sm font-medium text-gray-900" role="menuitem" tabIndex={-1} id="mobile-menu-item-2">Newest</a>
                        </div>
                    </div>
                    </div>

                    {/* Mobile filter dialog toggle, controls the 'mobileFilterDialogOpen' state. */}
                    <button type="button" className="inline-block text-sm font-medium text-gray-700 hover:text-gray-900 sm:hidden">Filters</button>

                    <div className="hidden sm:flex sm:items-baseline sm:space-x-8">
                    <div id="desktop-menu-0" className="relative inline-block text-left">
                        <div>
                        <button type="button" className="group inline-flex items-center justify-center text-sm font-medium text-gray-700 hover:text-gray-900" aria-expanded="false">
                            <span>Category</span>

                            <span className="ml-1.5 rounded bg-gray-200 py-0.5 px-1.5 text-xs font-semibold tabular-nums text-gray-700">1</span>
                            {/* Heroicon name: mini/chevron-down */}
                            <svg className="-mr-1 ml-1 h-5 w-5 flex-shrink-0 text-gray-400 group-hover:text-gray-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                            <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
                            </svg>
                        </button>
                        </div>

                        {/*
                        Entering: "transition ease-out duration-100"
                            From: "transform opacity-0 scale-95"
                            To: "transform opacity-100 scale-100"
                        Leaving: "transition ease-in duration-75"
                            From: "transform opacity-100 scale-100"
                            To: "transform opacity-0 scale-95"
                        */}
                        <div className="absolute right-0 z-10 mt-2 origin-top-right rounded-md bg-white p-4 shadow-2xl ring-1 ring-black ring-opacity-5 focus:outline-none">
                        <form className="space-y-4">
                            <div className="flex items-center">
                            <input id="filter-category-0" name="category[]" value="tees" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-category-0" className="ml-3 whitespace-nowrap pr-6 text-sm font-medium text-gray-900">Tees</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-category-1" name="category[]" value="crewnecks" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-category-1" className="ml-3 whitespace-nowrap pr-6 text-sm font-medium text-gray-900">Crewnecks</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-category-2" name="category[]" value="hats" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-category-2" className="ml-3 whitespace-nowrap pr-6 text-sm font-medium text-gray-900">Hats</label>
                            </div>
                        </form>
                        </div>
                    </div>

                    <div id="desktop-menu-1" className="relative inline-block text-left">
                        <div>
                        <button type="button" className="group inline-flex items-center justify-center text-sm font-medium text-gray-700 hover:text-gray-900" aria-expanded="false">
                            <span>Brand</span>
                            {/* Heroicon name: mini/chevron-down */}
                            <svg className="-mr-1 ml-1 h-5 w-5 flex-shrink-0 text-gray-400 group-hover:text-gray-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                            <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
                            </svg>
                        </button>
                        </div>

                        {/*
                        Entering: "transition ease-out duration-100"
                            From: "transform opacity-0 scale-95"
                            To: "transform opacity-100 scale-100"
                        Leaving: "transition ease-in duration-75"
                            From: "transform opacity-100 scale-100"
                            To: "transform opacity-0 scale-95"
                        */}
                        <div className="absolute right-0 z-10 mt-2 origin-top-right rounded-md bg-white p-4 shadow-2xl ring-1 ring-black ring-opacity-5 focus:outline-none">
                        <form className="space-y-4">
                            <div className="flex items-center">
                            <input id="filter-brand-0" name="brand[]" value="clothing-company" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-brand-0" className="ml-3 whitespace-nowrap pr-6 text-sm font-medium text-gray-900">Clothing Company</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-brand-1" name="brand[]" value="fashion-inc" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-brand-1" className="ml-3 whitespace-nowrap pr-6 text-sm font-medium text-gray-900">Fashion Inc.</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-brand-2" name="brand[]" value="shoes-n-more" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-brand-2" className="ml-3 whitespace-nowrap pr-6 text-sm font-medium text-gray-900">Shoes &#039;n More</label>
                            </div>
                        </form>
                        </div>
                    </div>

                    <div id="desktop-menu-2" className="relative inline-block text-left">
                        <div>
                        <button type="button" className="group inline-flex items-center justify-center text-sm font-medium text-gray-700 hover:text-gray-900" aria-expanded="false">
                            <span>Color</span>
                            {/* Heroicon name: mini/chevron-down */}
                            <svg className="-mr-1 ml-1 h-5 w-5 flex-shrink-0 text-gray-400 group-hover:text-gray-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                            <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
                            </svg>
                        </button>
                        </div>

                        {/*
                        Entering: "transition ease-out duration-100"
                            From: "transform opacity-0 scale-95"
                            To: "transform opacity-100 scale-100"
                        Leaving: "transition ease-in duration-75"
                            From: "transform opacity-100 scale-100"
                            To: "transform opacity-0 scale-95"
                        */}
                        <div className="absolute right-0 z-10 mt-2 origin-top-right rounded-md bg-white p-4 shadow-2xl ring-1 ring-black ring-opacity-5 focus:outline-none">
                        <form className="space-y-4">
                            <div className="flex items-center">
                            <input id="filter-color-0" name="color[]" value="white" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-color-0" className="ml-3 whitespace-nowrap pr-6 text-sm font-medium text-gray-900">White</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-color-1" name="color[]" value="black" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-color-1" className="ml-3 whitespace-nowrap pr-6 text-sm font-medium text-gray-900">Black</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-color-2" name="color[]" value="grey" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-color-2" className="ml-3 whitespace-nowrap pr-6 text-sm font-medium text-gray-900">Grey</label>
                            </div>
                        </form>
                        </div>
                    </div>

                    <div id="desktop-menu-3" className="relative inline-block text-left">
                        <div>
                        <button type="button" className="group inline-flex items-center justify-center text-sm font-medium text-gray-700 hover:text-gray-900" aria-expanded="false">
                            <span>Sizes</span>
                            {/* Heroicon name: mini/chevron-down */}
                            <svg className="-mr-1 ml-1 h-5 w-5 flex-shrink-0 text-gray-400 group-hover:text-gray-500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                            <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd" />
                            </svg>
                        </button>
                        </div>

                        {/*
                        Entering: "transition ease-out duration-100"
                            From: "transform opacity-0 scale-95"
                            To: "transform opacity-100 scale-100"
                        Leaving: "transition ease-in duration-75"
                            From: "transform opacity-100 scale-100"
                            To: "transform opacity-0 scale-95"
                        */}
                        <div className="absolute right-0 z-10 mt-2 origin-top-right rounded-md bg-white p-4 shadow-2xl ring-1 ring-black ring-opacity-5 focus:outline-none">
                        <form className="space-y-4">
                            <div className="flex items-center">
                            <input id="filter-sizes-0" name="sizes[]" value="s" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-sizes-0" className="ml-3 whitespace-nowrap pr-6 text-sm font-medium text-gray-900">S</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-sizes-1" name="sizes[]" value="m" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-sizes-1" className="ml-3 whitespace-nowrap pr-6 text-sm font-medium text-gray-900">M</label>
                            </div>

                            <div className="flex items-center">
                            <input id="filter-sizes-2" name="sizes[]" value="l" type="checkbox" className="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                            <label htmlFor="filter-sizes-2" className="ml-3 whitespace-nowrap pr-6 text-sm font-medium text-gray-900">L</label>
                            </div>
                        </form>
                        </div>
                    </div>
                    </div>
                </div>
                </section>
            </div>
        </div>
    )
}

export default Filters