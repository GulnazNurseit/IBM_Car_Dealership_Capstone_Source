# Coursera capstone evidence / submission guide

**This source code alone does not fulfill screenshot requirements.** Run the application and capture **actual browser/terminal views**. Keep the address bar visible on API and deployment pages. The app ships with sample fictional dealer entries in Kansas and other states.

| Task | Required evidence filename | Capture after |
|---|---|---|
| 1 | Public GitHub URL | Push this source to your own PUBLIC repo; use its real URL |
| 2 | django_server.png | Run Django `python manage.py runserver` or Docker logs |
| 3 | about_us.png | http://localhost:8000/about/ |
| 4 | contact_us.png | http://localhost:8000/contact/ |
| 5 | login.png | Login and capture authenticated home page |
| 6 | logout.png | http://localhost:8000/logout/ confirmation |
| 7 | sign-up.png | http://localhost:8000/signup/ |
| 8 | dealer_review.png | http://localhost:3000/fetchReview/dealer/1 |
| 9 | dealerships.png | http://localhost:3000/fetchDealers |
| 10 | dealer_details.png | http://localhost:3000/fetchDealer/1 |
| 11 | kansasDealers.png | http://localhost:3000/fetchDealers/Kansas |
| 12 | admin_login.png | http://localhost:8000/admin/ signed in as superuser |
| 13 | admin_logout.png | Django admin logged out |
| 14 | cars.png | http://localhost:8000/get_cars/ after adding makes and models in admin |
| 15 | car_models.png | Django admin CarModel list after adding models |
| 16 | sentiment_analyzer.png | http://localhost:5000/analyze/great%20service (local heuristic, not IBM Watson deployment) |
| 17 | get_dealers.png | Home page before logging in |
| 18 | get_dealers_loggedin.png | Home page logged in; Post Review is on dealer detail page |
| 19 | dealersbystate.png | http://localhost:8000/?state=Kansas |
| 20 | dealer_id_reviews.png | http://localhost:8000/dealer/1/ |
| 21 | dealership_review_submission.png | http://localhost:8000/dealer/1/review/ filled before submitting |
| 22 | added_review.png | Dealer 1 details showing submitted review |
| 23 | CICD.png | Successful real GitHub Actions workflow after pushing repo |
| 24 | Deployed URL | Needs a real cloud hosting deployment |
| 25 | deployed_landingpage.png | Real deployed URL in address bar |
| 26 | deployed_loggedin.png | Deployed URL after login |
| 27 | deployed_dealer_detail.png | Deployed URL dealer detail |
| 28 | deployed_add_review.png | Deployed URL showing posted review |

## Important gaps before full course credit
- Backend sentiment service is a **local keyword demo**, not IBM Watson NLU deployed to IBM Cloud Code Engine. Replace or deploy as required by lab.
- React client links to Django session-based auth pages; the complete review workflow is on the Django site. Verify the lab-specific React user-management screens before submitting evidence.
- The user must publish the repository and run GitHub Actions. This archive is not a public GitHub URL.
- The user must deploy and capture real screenshots; localhost URLs do NOT count as deployed URLs.
- The Django app needs a secure deployment configuration (secret key, DEBUG off, allowed hosts, CSRF origins, HTTPS, persistent database and static files).
