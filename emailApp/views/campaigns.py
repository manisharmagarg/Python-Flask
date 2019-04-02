from emailApp import *
from emailApp.views.baseview import BaseView


class Campaigns(BaseView):

	def __init__(self):
		self.context = dict()

	def get_template_name(self):
		return 'campaigns/campaigns.html'

	@login_required
	def get(self):
		return self.render_template(self.context)

	def post(self):
		pass

"""
email_campaign = campaign_helper_obj.get_campaigns()
    email_ab_campaign = ab_campaigns_helper_obj.get_all_ab_campaign()

    email_campaigns = []

    for item in email_campaign:
        email_campaign_data = []
        id = item['id']
        campaign_type = item['campaign_type']
        name = item['name']
        campaign_state = item['campaign_state']
        status = item['status']

        email_campaign_data.append(id)
        email_campaign_data.append(name)
        email_campaign_data.append(campaign_type)
        email_campaign_data.append(status)
        email_campaign_data.append(campaign_state)

        email_campaigns.append(email_campaign_data)

    for ab_data in email_ab_campaign:
        email_campaign_data = []

        id = ab_data['id']
        camapaign_type = ab_data['campaign_type']
        name = ab_data['name']
        campaign_state = ab_data['campaign_state']
        status = ab_data['status']

        email_campaign_data.append(id)
        email_campaign_data.append(name)
        email_campaign_data.append(camapaign_type)
        email_campaign_data.append(status)
        email_campaign_data.append(campaign_state)

        email_campaigns.append(email_campaign_data)

    all_campaigns = sorted(email_campaigns, key=lambda x: x[3], reverse=True)
    context = {'email_campaigns': all_campaigns,
               'One_time': email_campaign,
               'AB_test': email_ab_campaign}
    return render_template('campaigns/campaigns.html', **context)
"""