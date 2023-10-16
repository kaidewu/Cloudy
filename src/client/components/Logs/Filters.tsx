const Filters = () => {
    return (
        <div>
            <div className="bg-grey col-12 mt-3 align-middle justify-content-center flex" >
				<button type="button" className="btn btn-light mr-10 shadow-sm" data-toggle="collapse" data-target="#filters">Filters <i className="fa fa-filter"></i></button>
				<input type="text" className="col-8 border-2 p-2" placeholder="Search for Startups..." id="search-filter"/>
			</div>

			<div id="filters" className="collapse">
				<hr className="solid col-9 mx-auto">

				<div className="d-md-flex d-lg-flex d-xl-flex justify-content-around col-9 mx-auto">

				<div className="col-lg-4 col-xl-3 col-md-6">
					<article className="filter-group">
						<header className="card-header"> 
								<h6 className="title">Domain </h6>
						 </header>
							<div className="filter-content" id="collapse_aside1" style={}>
								<div className="card-body"> <label className="custom-control"> <input type="checkbox" checked={} className="custom-control-input"/>
										<div className="custom-control-label"> E-commerce </div>
									</label> <label className="custom-control"> <input type="checkbox" checked={} className="custom-control-input"/>
										<div className="custom-control-label"> Education </div>
									</label> <label className="custom-control"> <input type="checkbox" checked={} className="custom-control-input"/>
										<div className="custom-control-label"> Aggriculture</div>
									</label> <label className="custom-control"> <input type="checkbox" checked={} className="custom-control-input"/>
										<div className="custom-control-label"> Service</div>
									</label> </div>
							</div>
					</article>
					<article className="filter-group">
						<header className="card-header"> 
							<h6 className="title"> Team Size </h6>
						</header>
						<div className="filter-content" id="collapse_aside3" style={}>
							<div className="card-body"> 
								<label className="checkbox-btn"> <input type="checkbox" name="team" onclick="onlyOne(this)"> <span className="btn btn-light"> 1 - 10 </span> </label>
								<label className="checkbox-btn"> <input type="checkbox" name="team" onclick="onlyOne(this)"> <span className="btn btn-light"> 10 - 25 </span> </label> 
								<label className="checkbox-btn"> <input type="checkbox" name="team" onclick="onlyOne(this)"> <span className="btn btn-light"> 25 - 50 </span> </label> 
								<label className="checkbox-btn"> <input type="checkbox" name="team" onclick="onlyOne(this)"> <span className="btn btn-light"> 50 - 100 </span> </label> 
								<label className="checkbox-btn"> <input type="checkbox" name="team" onclick="onlyOne(this)"> <span className="btn btn-light"> greater than 100 </span> </label> 
							</div>
						</div>
					</article>
					
				</div>
				
				<div class ="col-lg-4 col-xl-3 col-md-6">

					<article className="filter-group">
						<header className="card-header"> 
							<h6 className="title">Assistance Required </h6>
						</header>
						<div className="filter-content" id="collapse_aside1" style={}>
							<div className="card-body"> <label className="custom-control"> <input type="checkbox" checked={} className="custom-control-input">
									<div className="custom-control-label"> Under 50,000 &#8377; </div>
								</label> <label className="custom-control"> <input type="checkbox" checked={} className="custom-control-input">
									<div className="custom-control-label"> 50,000 - 1 L &#8377; </div>
								</label> <label className="custom-control"> <input type="checkbox" checked={} className="custom-control-input">
									<div className="custom-control-label"> 1 L - 5 L &#8377;</div>
								</label> <label className="custom-control"> <input type="checkbox" checked={} className="custom-control-input">
									<div className="custom-control-label"> More than 5 L &#8377;</div>
								</label> </div>
						</div>
						
					</article>
					<article className="filter-group">
						<header className="card-header"> 
							<h6 className="title"> Year </h6>
						</header>
						<div className="filter-content" id="collapse_aside1" style=" height: fit-content;">
						<input className="date-own form-control mb-10 overscroll-auto" style={} type="text">


						<script type="text/javascript">
							$('.date-own').datepicker({
							   minViewMode: 2,
							   format: 'yyyy'
							 });
						</script>
						</div>
					</article>
					
					
				</div>
				<div class ="col-lg-4 col-xl-3 col-md-6">
					<article className="filter-group">
						<header className="card-header"> 
							<h6 className="title">Stage </h6>
						</header>
						<div className="filter-content" id="collapse_aside4" style={}>
							<div className="card-body"> <label className="custom-control"> <input type="checkbox" checked={} className="custom-control-input">
									<div className="custom-control-label"> Completed </div>
								</label> <label className="custom-control"> <input type="checkbox" checked={} className="custom-control-input">
									<div className="custom-control-label"> Processing </div>
								</label> <label className="custom-control"> <input type="checkbox" checked={} className="custom-control-input">
									<div className="custom-control-label"> Pending</div>
								</label> <label className="custom-control"> <input type="checkbox" checked={} className="custom-control-input">
									<div className="custom-control-label"> Something else</div>
								</label> </div>
						</div>
					</article>
					
					<a href="#" className="btn btn-medium button mt-6 mb-12 md:mb-0 md:mt-10 inline-block  text-white bg-red-500 hover:bg-red-600 rounded-lg shadow mx-auto" data-abc="true" data-toggle="collapse" data-target="#filters">Apply Now</a>

				</div>

				</div>
				
				
						</div>
					</div>
				</div>
			</div>
			</div>

				
			</div>
		</div>
        </div>
    )
}

export default Filters