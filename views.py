#changed variable names for security purpose
class MoodsView(View):
    @strap_page(False)
    def get(self, request, *args, **kwargs):
        page_data = kwargs['page_data']
        template_name='moods.html'

        if 'name' in self.kwargs:
            page_data['category'] = getModules(request, self.kwargs['name'], page_data['regionUrls']['curTer'], 'slug')
        else:
            page_data['category'] = getModules(request, 'anime-classics', page_data['regionUrls']['curTer'], 'slug')

        if page_data['category'] and len(page_data['category']['items']) > 0 and len(page_data['category']['items'][0]['content']) > 0:
            page_data['category'] = page_data['category']['items'][0]
            page_data['modules'] = getModules(request, "moodsv2", page_data['regionUrls']['curTer'])
            page_data['headerPlacement'] = []
            if 'items' in page_data['modules']:
                newItems = []
                if 'items' in page_data['modules']:
                    for m in page_data['modules']['items']:
                        if 'top-placement' in m['customClass'] and m['type'] == 'html_block':
                            page_data['headerPlacement'].append(m)
                        else:
                            newItems.append(m)
                    page_data['modules']['items'] = newItems
            return render(request,template_name, page_data)
        else:
            return show_404(request, {})

