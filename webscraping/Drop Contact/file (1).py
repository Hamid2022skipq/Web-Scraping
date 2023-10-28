"""
Graphql query that I used to get the data from the API:
query BigListQuery($name_or_firm: String, $name: String, $mode: String, $amount_range: [String], $firm_ids: [ID!], $position: [String!], $location_id: String, $location_kind: LocationKind, $interest_tag_ids: [String!], $past_investment_ids: [String!], $position_company_ids: [String!], $school_ids: [String!], $is_lead: Boolean, $order: [QuerySorting!], $after: String, $first: Int, $stage_ids: [ID!]) {
  investors(first: $first, after: $after, name_or_firm: $name_or_firm, name: $name, mode: $mode, amount_range: $amount_range, firm_ids: $firm_ids, position: $position, location_id: $location_id, location_kind: $location_kind, interest_tag_ids: $interest_tag_ids, past_investment_ids: $past_investment_ids, position_company_ids: $position_company_ids, school_ids: $school_ids, is_lead: $is_lead, order: $order, stage_ids: $stage_ids) {
    record_count
    edges {
      cursor
      node {
        ...investorListInvestorProfileFields
      }
    }
  }
}

fragment investorListInvestorProfileFields on InvestorProfile {
  id
  headline
  person {
    id
    slug
    first_name
    last_name
    name
    linkedin_url
    facebook_url
    twitter_url
    crunchbase_url
    angellist_url
    roles
    url
    email
    is_on_target_list
    first_degree_count
    relationship_strength
    email_from_my_contacts_list
  }
  stages {
    kind
    display_name
  }
  investment_locations {
    kind
    display_name
  }
  location {
    display_name
  }
  position
  min_investment
  max_investment
  target_investment
  headline
  previous_position
  previous_firm
  areas_of_interest_freeform
  no_current_interest_freeform
  vote_count
  firm {
    name
  }
  degrees {
    id
    name
    field_of_study
    school {
      id
      name
      display_name
      total_student_count
    }
  }
  investments_on_record(last: 5) {
    pageInfo {
      hasNextPage
    }
    record_count
    edges {
      node {
        id
        company_display_name
        total_raised
        coinvestor_names
        investor_profile_funding_rounds {
          id
          is_lead
          board_role {
            id
            title
          }
          funding_round {
            id
            stage
            date
            amount
          }
        }
      }
    }
  }
}
data is saved in new_data.json
"""
import csv
import json
with open('new_data.json') as f:
    data = json.load(f)

# need to clean the data first 
new_data = []
for i in range(len(data['data']['investors']['edges'])):
    new_data.append(data['data']['investors']['edges'][i]['node'])

# need to clean investments_on_record

for i in range(len(new_data)):
  new_data[i]['investments_on_record'] = [inv['node'] for inv in new_data[i]['investments_on_record']['edges']]

  new_data[i]['degrees'] = [degree for degree in new_data[i]['degrees']]
  new_data[i]['firm'] = new_data[i]['firm']['name'] if new_data[i]['firm'] else None
  new_data[i]['location'] = new_data[i]['location']['display_name'] if new_data[i]['location'] else None
  new_data[i]['investment_locations'] = ", ".join([loc['display_name'] for loc in new_data[i]['investment_locations']])
  new_data[i]['stages'] = ", ".join([stages['display_name'] for stages in new_data[i]['stages']])
  for user in new_data[i]['person']:
    new_data[i][user] = new_data[i]['person'][user]
  del new_data[i]['person']

# convert to csv
with open('new_data.csv', 'w', newline='') as csvfile:
    fieldnames = new_data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(new_data)):
        writer.writerow(new_data[i])
