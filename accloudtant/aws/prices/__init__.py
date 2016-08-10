#!/usr/bin/env python
#   Copyright 2015-2016 See CONTRIBUTORS.md file
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from accloudtant.aws.prices.web import WebPrices


class Prices(object):
    def __init__(self, source=None):
        if source is None:
            source = 'Web'
        self.source = source
        if self.source == 'Web':
            self.web = WebPrices()

    @property
    def prices(self):
        if self.source == 'Web':
            return self.web.prices

    @property
    def output(self):
        if self.source == 'Web':
            return self.web.output

    def __repr__(self):
        return self.output
